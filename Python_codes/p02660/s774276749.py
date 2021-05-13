import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.debug("デバッグスタート")  #

n = int(input())
a = []
b = 1
while n % 2**b == 0:
    a.append(2**b)
    n /= 2**b
#    logging.debug("n = {},b = {}".format(n,2 ** b))  #
    b += 1

while n % 2 == 0:
    n /= 2

f = 3
b = 1
while f * f <= n:
    if n % f**b == 0:
        a.append(f**b)
        n /= f**b
        b += 1
    else:
        while n % f == 0:
            n /= f
        f += 2
        b = 1
#    logging.debug("n = {},f = {},f**b = {}".format(n, f, f**b))  #
if n != 1:
    a.append(n)

#print(a)
print(len(set(a)))
#logging.debug("デバッグ終了")#