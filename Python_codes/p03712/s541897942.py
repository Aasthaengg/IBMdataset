h,w = map(int,input().split())
s =list()
for i in range(h):
    s.append(list(input()))

print("".join(["#" for _ in range(w+2)]))
for j in range(h):
    s[j].insert(0,"#")
    s[j].append("#")
    print("".join(s[j]))
print("".join(["#" for _ in range(w+2)]))