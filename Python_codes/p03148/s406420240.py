# めちゃよかったのでほぼそのまま　https://atcoder.jp/contests/abc116/submissions/4060186?lang=ja
import heapq
import sys
input = sys.stdin.readline

def main():
	[N,K]=[int(x) for x in input().split()]
	td=[[int(x) for x in input().split()] for _ in range(N)]
	td.sort(key=lambda x:x[1],reverse=True)
	
	# 貪欲にとる.
	keep = []  # 各種類のsushiでおいしさ最大のものを保存
	exchange = []  # 取り替える用 (種類がかぶっているものが入る). priority queue
	types = set() # keepに入っているsushiの種類
	for i in range(K):
	    [t, d] = td[i]
	    if t not in types:
	        keep.append(d)
	        types.add(t)
	    else:
	        heapq.heappush(exchange, d)
	 
	basic_point_1 = sum(keep)
	basic_point_2 = sum(exchange)
	types_bonus = len(types)
	ans = basic_point_1 + basic_point_2 + types_bonus**2
	 
	# 種類が増えるようにおいしさ最大のものから交換していく.
	for i in range(K, N):
	    if len(exchange) == 0:  # 取り替えると種類が減るので終了.
	        break
	    [t, d] = td[i]
	    if t in types:
	        continue
	    types.add(t)
	    basic_point_1 += d
	    basic_point_2 -= heapq.heappop(exchange) # おいしさ最小のものと交換.
	    types_bonus += 1
	    ans = max(ans, basic_point_1 + basic_point_2 + types_bonus**2)
	print(ans)
        
if __name__ == "__main__":
  main()
    
