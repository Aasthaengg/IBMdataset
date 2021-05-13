N = int(input())
S = input()
count = 0
for i in range(10):
    #print(S.find(str(i)),i)
    if S.find(str(i)) == -1:
        #print(S.find(str(i)),i)
        continue
    for j in range(10):
        if S.find(str(j),S.find(str(i))+1) == -1:
            #print(S.find(str(j)),j)
            continue
        for k in range(10):
            if S.find(str(k),S.find(str(j),S.find(str(i))+1)+1) != -1:
                #print(S.find(str(k)),k)
                count += 1
print(count)
