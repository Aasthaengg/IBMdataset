a,b,c,d = map(int,input().split())
dict = {}
dict[a] = 1
dict[b] = 1
dict[c] = 1
dict[d] = 1
if 1 in dict and 9 in dict and 7 in dict and 4 in dict:
    print("YES")
else:
    print("NO")
