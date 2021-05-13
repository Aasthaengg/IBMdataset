import numpy as np

n,m,d = map(int,input().split())

"""
#kuso code
start = time.time()
a = [random.randrange(n) for i in range(m)]
a = np.array(a)
b = np.abs(a[1:]-a[:-1])
cnt = np.sum(b == d)
ave = cnt

i = 0
while(time.time() - start < 10):
    a = [random.randrange(n) for i in range(m)]
    a = np.array(a)
    b = np.abs(a[1:]-a[:-1])
    cnt = np.sum(b == d)
    ave = ((i+1)*ave + cnt)/(i+2)
    i += 1
print(ave)
"""

oks_times_n = 2*np.max(n-2*d,0) + 2*d
ave = oks_times_n/n/n*(m-1)
if (d == 0):
    ave /= 2
print(ave)
