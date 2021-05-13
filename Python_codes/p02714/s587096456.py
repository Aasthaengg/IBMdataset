n = int(input())
s = input()

su = s.count('R') * s.count('G') * s.count('B')
for i in range(n):
    for j in range(i+1,n):
        if s[i] != s[j]:
            for lis in ['R','G','B']:
                if lis != s[i] and lis != s[j]:
                    try:
                        su -= s[2*j-i].count(lis)
                    except:
                        pass

print(su)