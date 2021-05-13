a, b, x = map(int,input().split())



## ことごとくTLEする件
# forを回すからだめなのかも→回さないですませるには？
# bまでに約数いくつあるか出す → a-1 までに約数いくつあるか出す→引き算



## まず、aが割り切れるかどうか判定
## aが割り切れるなら、最小値はa
## 割り切れないなら、a+（除数 - あまり ) が最小値

#### divmodを使ってみよう！！


result = 0

a_x = divmod(a,x)  ## a/x の商と余り
## a = x * a_x[0] + a_x[1]
if a_x[1]==0:  ## 割り切れるとき
    first = a
else:  ## 割り切れないとき
    first = x * (a_x[0]+1)
    first2 = a + (x - a_x[1])  ## 検算用


b_x = divmod(b-first, x)

result = b_x[0]+1

print(result)






"""
名答だと思ったがだめだった

count = 0
first = 0
for i in range(a, b+1):
#    print(i)
    if i%x == 0:
        first = i
        count = 1
        break
    
if count != 0:
    result  = (b-first) // x +1

else :
    result = 0


print(result)



"""

