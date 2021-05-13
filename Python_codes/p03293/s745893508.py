def kaiten(x):
    a=x[:-1]
    x=x[-1:]
    return x+a


S=str(input())
T=str(input())
ans="No"
for i in range(len(S)):
    if S==T:
        ans="Yes"
        break
    S=kaiten(S)

print(ans)