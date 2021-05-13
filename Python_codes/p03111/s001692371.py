
N,A,B,C = map(int, input().split())
bamboos = [int(input()) for _ in range(N)]
#print("---", bamboos)
ans = float("inf")
def solve(lst, idx):
    global ans
    if idx == N:
        #print("qqqqq")
        for i in range(3):
            if len(lst[i]) == 0:
                return

        
        pa = 10 * (len(lst[0])-1) + abs(A - sum(lst[0]))
        pb = 10 * (len(lst[1])-1) + abs(B - sum(lst[1]))
        pc = 10 * (len(lst[2])-1) + abs(C - sum(lst[2]))
        #print(pa, pb, pc, lst)
        ans = min(ans, pa + pb + pc)
        #print("aaaaaaa")
        return

    
    for i in range(4):
        nxt_lst = [lst[0][:], lst[1][:], lst[2][:], lst[3][:]]
        nxt_lst[i].append(bamboos[idx])
        #print(lst, nxt_lst)
        
        solve(nxt_lst, idx+1)

empty_lst =  [[], [], [], []]   
solve(empty_lst, 0)
print(ans)