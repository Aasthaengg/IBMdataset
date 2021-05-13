## coding: UTF-8

N = int(input())
l = []
for i in range(N):
    l.append(input())

#print(N)
#print(l)

#中にあるABの数を数える
def count_inAB(s):
    counter = 0
    for i in range(len(s)-1):
        if(s[i] == 'A' and s[i+1] == 'B'):
            counter += 1
    return counter
'''
print(count_inAB('ABCA'))
print(count_inAB('ABCAB'))
print(count_inAB('ABABAB'))
print(count_inAB('ACBA'))
'''
#末尾にあるAの数を数える
lastA = []
for i in range(N):
    if(l[i][-1] == 'A'):
        lastA.append(i)
#print('lastA:{}'.format(lastA))

#先頭にあるBの数を数える
firstB = []
for i in range(N):
    if(l[i][0] == 'B'):
        firstB.append(i)
#print('firstB:{}'.format(firstB))






ans = 0
for i in range(N):
    ans += count_inAB(l[i])
    #print(ans)
#print('insert:{}'.format(ans))


connect = min(len(lastA), len(firstB))
if(lastA == firstB):
    connect -= 1
if(lastA == [] and firstB == []):
    connect += 1
#print('connect:{}'.format(connect))


ans += connect

#rint('ans:{}'.format(ans))
print(ans)