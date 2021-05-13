R,G,B,N=map(int,input().split())

numbers=[R,G,B]
new_numbers=sorted(numbers,reverse=True)
a=new_numbers[0]
b=new_numbers[1]
c=new_numbers[2]

answer=0

for n in range(N//a+1):
    A=a*n
    B=N-A
    for n_ in range(B//b+1):
        C=n_*b
        D=B-C
        if D%c==0:
            answer+=1
print(answer)
