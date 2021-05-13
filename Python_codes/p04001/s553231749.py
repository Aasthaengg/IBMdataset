S=input()
num = len(S)-1 #符号を加えられる隙間の数
x=[]

for i in range(2**num):
    tmp=['-']*num #すべてマイナスを初期値として用意しておく
    for j in range(num):
        if ((i >> j) &1):
            tmp[num-1-j] ='+'
    x.append(tmp)
        
#print(x) #これで全符号パターンができた

ans =0

for i in range(len(x)):
    now =S[0]
    for j in range(len(x[i])):
        if x[i][j] == '-':
            now += S[j+1:j+2]
        else:
            now = now + x[i][j] + S[j+1:j+2] 
    #print(now) #プラスの記号を挿入した表記
    ans += eval(now)

print(ans)