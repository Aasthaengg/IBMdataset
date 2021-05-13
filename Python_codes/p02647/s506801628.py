from numba import jit
@jit
def main():
    n,k = map(int,input().split())
    lamps = list(map(int,input().split()))
    for ki in range(k):
        lamplog = [0]*(n+1)
        for i in range(n):
            lamplog[max(0,i-lamps[i])  ] += 1   #先端を出す
            lamplog[min(i+lamps[i]+1,n)] -= 1   #末尾を出す
        # print(lamplog)
        for i in range(n):                      #累積和を計算
            lamplog[i+1] += lamplog[i]
        # print(lamplog)
        lamplog.pop()
        if(lamplog == lamps):                   #１つ前の結果と今回の結果が同じだったら。
            break
        lamps = lamplog                         #今回の結果を記録
    return lamplog

lamplog = main()
ans = ""
for i in range(len(lamplog)):
    ans += str(lamplog[i]) +" "
print(ans.rstrip())