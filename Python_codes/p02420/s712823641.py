#60 シャッフル

s = input()
while s !="-":
        m = int(input())
        h = 0
        
        for i in range(m):
            h += int(input())
            h %= len(s)
            s1 = s[h : len(s)] + s[0 : h]
        print(s1)
        
        s = input()
