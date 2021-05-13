import bisect
 
a, b, q = map(int, input().split())
s = [float('-inf')] + [int(input()) for _ in range(a)] + [float('inf')]
t = [float('-inf')] + [int(input()) for _ in range(b)] + [float('inf')]
 
 
for _ in range(q):
    
    x = int(input())
    
    s_index = bisect.bisect_right(s, x)
    s_right = s[s_index]
    s_left = s[s_index - 1]
    t_index = bisect.bisect_right(t, x)
    t_right = t[t_index]
    t_left = t[t_index - 1]
    
    ans = float('inf')
    
    # 最初に寺を訪れる場合
    ans = min(
        ans, 
        abs(x - s_right) + min(abs(s_right - t_right), abs(s_right - t_left)), 
        abs(x - s_left) + min(abs(s_left - t_right), abs(s_left - t_left)), 
    )
    # 最初に神社を訪れる場合
    ans = min(
        ans, 
        abs(x - t_right) + min(abs(t_right - s_right), abs(t_right - s_left)), 
        abs(x - t_left) + min(abs(t_left - s_right), abs(t_left - s_left)), 
    )
        
    print(ans)