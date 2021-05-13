n = int(input())
s = input()

S = set()
cnt = 0

for i in range(10):
    for j in range(10):
        for k in range(10):
            dig = 1
            t = str(i)+str(j)+str(k)

            for r in range(n):
                if dig == 1 and t[0] == s[r]:
                    dig +=1

                elif dig == 2 and t[1] == s[r]:
                    dig +=1
                    
                elif dig == 3 and t[2] == s[r]:
                    S.add(t)

print(len(S))