n = int(input())
#√nまでの素数の配列を返す関数
def primes(n):
    if n < 4:
        return []
    else:
        pri = [2]
        k = 3
        while k*k <= n:
            for i in pri:
                if k%i == 0:
                    break
                elif i == pri[-1]:
                    pri.append(k)
            k += 2
        return pri

ps = primes(55555**2)
p1 = []
for i in ps:
    if i%10 == 1:
        p1.append(i)
    if len(p1) == n:
        break

print(" ".join(map(str,p1)))
