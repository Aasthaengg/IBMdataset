n = int(input())
a_input = list(map(int,input().split()))

#a_i*a_(i+1)が4の積になるにはeven*even or ood*4の倍数であることが必要
#奇数を数えて、odd,4,...4,odd,4...4,oddにできるか判定
#odd,4,odd,4,odd,4...が最小
#odd,4,odd,4,odd
#if len(odd)+len(4)-1==n: yes
#else:len(odd)<=len(4):yes

odd=0
multiple4=0

for i in range(n):
    a = a_input[i]
    if a%2!=0:
        odd+=1
    if a%4==0:
        multiple4+=1

if odd+multiple4==n and odd-multiple4==1:print('Yes');exit()
if odd<=multiple4:print('Yes');exit()
print('No')
