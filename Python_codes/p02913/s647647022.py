alphabetlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet={moji:alphabetlist.index(moji) for moji in alphabetlist}

N=int(input())
S=input()

def condition(num):
    if num==0:
        return True

    data=[]
    x=0
    for i in range(num):
        x+=alphabet[S[i]]*26**i

    data.append((x,0))

    for i in range(0,N-num+1):
        if i==0:
            continue
        else:
            x=x//26+alphabet[S[i+num-1]]*26**(num-1)
            data.append((x,i))

    data.sort()
    min=data[0][1]
    max=data[0][1]
    for i in range(0,len(data)-1):
        if data[i][0]==data[i+1][0]:
            max=data[i+1][1]
        else:
            if max-min>=num:
                return True
            min=data[i+1][1]
            max=data[i+1][1]

    if max-min>=num:
        return True

    return False

start=0
end=N
while end-start>1:
    test=(end+start)//2
    if condition(test):
        start=test
    else:
        end=test

if condition(end):
    print(end)
else:
    print(start)