n = int(input())
s, t = map(str, input().split())
ans = [s_+t_ for s_,t_ in zip(s,t)]
print("".join(ans))