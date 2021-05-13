N=int(input())
S=input()

def condition(num):
    data=[]
    for i in range(0,N-num+1):
        data.append((S[i:i+num],i))

    data.sort()
    if len(data)==1:
        return False

    small=data[0][1]
    large=data[0][1]
    for i in range(0,len(data)-1):
        if data[i][0]==data[i+1][0]:
            large=data[i+1][1]
        else:
            if large-small>=num:
                return True
            else:
                small=data[i+1][1]
                large=data[i+1][1]

    if large-small>=num:
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