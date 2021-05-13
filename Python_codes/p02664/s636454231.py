def find(S):
    ans = []
    for x in S:
        if x == "?":
            ans+=["D"]
        else:
            ans+=[x]
    return "".join(ans)
print(find(input()))