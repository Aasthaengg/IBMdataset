N = list(map(int,input().split()))
q = int(input())

for _ in range(q):
    problem = [int(x) for x in input().split()]
    
    
    if problem in [[N[0],N[1]],[N[1],N[5]],[N[5],N[4]],[N[4],N[0]]]:
        print(N[2])
    elif problem in [[N[3],N[1]],[N[1],N[2]],[N[2],N[4]],[N[4],N[3]]]:
        print(N[0])
    elif problem in [[N[3],N[5]],[N[5],N[2]],[N[2],N[0]],[N[0],N[3]]]:
        print(N[1])
    elif problem in [[N[4],N[5]],[N[5],N[1]],[N[1],N[0]],[N[0],N[4]]]:
        print(N[3])
    elif problem in [[N[2],N[5]],[N[5],N[3]],[N[3],N[0]],[N[0],N[2]]]:
        print(N[4])
    elif problem in [[N[1],N[3]],[N[3],N[4]],[N[4],N[2]],[N[2],N[1]]]:
        print(N[5])

