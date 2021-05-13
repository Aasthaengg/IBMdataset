A,B,C,D,E,F = map(int,input().split())

nou = [0,100*A]
for a in range(31):
    for b in range(31):
        for c in range(3001):
            if a==0 and b==0:
                continue
            if F<(100*A*a+100*B*b+C*c):
                continue
            if E*(A*a+B*b)<C*c:
                continue
            #abcが決まればdはEとFの上限を超えないギリギリを責めればいい
            d = max(0, (F-(100*A*a+100*B*b+C*c))//D)#Fの条件
            d = min(d,(E*(A*a+B*b)-C*c)//D)

            if nou[0]*((100*A*a+100*B*b)+(C*c+D*d)) < (C*c+D*d)*nou[1]:
                nou = [C*c+D*d,((100*A*a+100*B*b)+(C*c+D*d)),a,b,c,d]

print(nou[1],nou[0])