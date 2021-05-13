def main():

    N = int(input())
    a = int(input())
    A = [a]

    if a != 0:
        return -1

    else:
        for i in range(N-1):
            a_ = int(input())
            if a_ > a + 1:
                return -1

            else:
                a =  a_
                A.append(a)
            
        count = 0
        for i in range(N-1):
            a = A[N-1-i]
        
            if a == 0:
                continue
            elif a == A[N-2-i] + 1:
                count += 1
            else:
                count += a
                
        return count

print(main())