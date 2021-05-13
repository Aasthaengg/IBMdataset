

def main():
    X,Y,A,B,C  = map(int, input().split()) 
    sum = 0
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))
    list.sort(p,reverse=True)
    list.sort(q,reverse=True)
    list.sort(r,reverse=True)
    strr = len(r)
    pq = []


    rindex = 0

    for index in range(X):
        sum += p[index]
        pq.append(p[index])

    for index in range(Y):
        sum += q[index]
        pq.append(q[index])

    list.sort(pq,reverse=True)
    strpq = len(pq)

    for index in range(strr):
        if strpq > index and r[index] > pq[X+Y-1-index]:
            sum += r[index] - pq[X+Y-1-index]

    print (sum)


if __name__ == '__main__':
    main()
