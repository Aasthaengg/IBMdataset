from heapq import heapify, heappush, heappop

def main():
    n, m = map(int, input().split())
    a = [int(x)*-1 for x in input().split()]
    ans = sum(a)*-1
    diff = 0
    
    heapify(a)
    for _ in range(1, m+1):
        _h_a = heappop(a) * -1
        diff += _h_a - _h_a // 2
        heappush(a, (_h_a // 2)*-1)
    ans -= diff
    print(ans)
    
if __name__ == '__main__':
    main()