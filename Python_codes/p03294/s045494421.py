import sys
sys.setrecursionlimit(1000000)
#def input():
#    return sys.stdin.readline()[:-1]

'''
n=int(input())
for i in range(n):
    a[i]=int(input())
    a[i],b[i]=map(int,input().split())
a=[int(x) for x in input().split()]
n,m=map(int,input.split())

'''

test_data1 = '''\
A??C
'''

test_data2 = '''\
ACACAC
'''

test_data3 = '''\
7
994 518 941 851 647 2 581
'''

test_data4 = '''\
?AC?AC
'''
td_num=3

def GetTestData(index):
    if index==1:
        return test_data1
    if index==2:
        return test_data2
    if index==3:
        return test_data3
    if index==4:
        return test_data4
    
if False:
    with open("../test.txt", mode='w') as f:
        f.write(GetTestData(td_num))
    with open("../test.txt") as f:
        # Start Input code ---------------------------------------
        n=int(f.readline())
        a=[int(x) for x in f.readline().split()]
        # End Input code ---------------------------------------
else:
    # Start Input code ---------------------------------------
    n=int(input())
    a=[int(x) for x in input().split()]
    # End Input code ---------------------------------------
#print(n,a,sum(a)-n)
print(sum(a)-n)
