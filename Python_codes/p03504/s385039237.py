import sys

input = sys.stdin.readline

def main():
    N, C = map(int, input().split())
    
    event = []
    
    for i in range(N):
        s, t, c = map(int, input().split())
        event.extend([[s, c-1, 1], [t+0.5, c-1, 0]])
        
    event.sort()
    
    nums = [0] * C
    ans = cur = 0
    
    for e, c, m in event:
        if m:
            if not nums[c]: 
                cur += 1
                ans = max(ans, cur)
            nums[c] += 1
        else:
            nums[c] -= 1
            if not nums[c]: cur -= 1
            
    print(ans)

if __name__ == '__main__':
    main()
