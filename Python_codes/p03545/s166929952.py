import itertools

S=input()

for i in itertools.product(["+","-"],repeat=3):
    ans=""
    for j in range(len(i)):
        if i[j]=="+":
            ans+=S[j]+i[j]
        elif i[j]=="-":
            ans+=S[j]+i[j]
    ans+=S[-1]
    sum_num=eval(ans)
    if sum_num==7:
        print(ans+"=7")
        break
