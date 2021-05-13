H,W = map(int, input().split())
s = []
for i in range(H):
    a = "#"+input()+"#"
    s.append(a)
s.insert(0,"#"*(W+2))
s.append("#"*(W+2))
for i in range(H+2):
    print(''.join(s[i]))