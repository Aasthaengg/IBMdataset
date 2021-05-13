abc=list(map(int,input().split()))
abc.sort(reverse=True)
if abc[0]-abc[1]==abc[1]-abc[2]:
    print("YES")
else:
    print("NO")
