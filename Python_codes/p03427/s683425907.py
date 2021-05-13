n =input()

#最上位の桁をc,桁数をkとすると、
#c以外が9の場合(ex.49999)はc,9*(k-1)となる
#それ以外の場合、c,9*(k-2),8となる(ex.9995:9989)

c = int(n[0])
k = len(n)
if int(n)<10:
    print(n);exit()
if int(n[1:])==int('9'*(k-1)):
    ans = c+9*(k-1)
else:
    ans = c+9*(k-1)-1

print(ans)
