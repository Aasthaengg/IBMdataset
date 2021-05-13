def solve(s,w):
    if w>=s:
        return "unsafe"
    else:
        return 'safe'


s,w = map(int,input().split())
print(solve(s,w))