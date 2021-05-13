def issafe(S,W):
    if S > W:
        return "safe"
    return "unsafe"

S,W = map(int,input().split())
print(issafe(S,W))
