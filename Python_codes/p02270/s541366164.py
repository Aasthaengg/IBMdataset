n,k = [int(x) for x in input().split()]

w = []

for i in range(n):
        w.append(int(input()))

def f(p, k, w):
        tmpk = 0
        tmpw = 0
        cnt = 0

        for i in w:
                if tmpk < k - 1:
                        if tmpw + i <= p:
                                tmpw += i
                                cnt += 1
                        else:
                                if i <= p:
                                        tmpk += 1
                                        tmpw = i
                                        cnt += 1
                                else:
                                        break
                else:
                        if tmpw + i <= p:
                                tmpw += i
                                cnt += 1
                        else:
                                break
        return cnt

    
pmin = 1
pmax = sum(w)

while pmin < pmax:
        mid = (pmin + pmax) // 2
        tmp = f(mid, k , w)

        if tmp < n:
                pmin = mid + 1
        else:
                pmax = mid

print(pmin)