def resolve():
    K,A,B = map(int,input().split())
    if A>=B or K<=A:
        print(K+1)
        return
    
    nokori = K-A+1
    diff = B-A

    sc = A+ + diff*(nokori//2) +(1 if nokori%2 ==1 else 0)
    print(max(sc,K+1))
resolve()
