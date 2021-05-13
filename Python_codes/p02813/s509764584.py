import itertools
#itertools.permutations(t)

def main():
    n = int(input())
    p = tuple(map(int, input().split(" ")))
    q = tuple(map(int, input().split(" ")))

    n_list = [i+1 for i in range(n)]
    n_perm = list(itertools.permutations(n_list))
    
    for i, one in enumerate(n_perm):
        i1 = i + 1
        if one==p:
            a = i1
        if one==q:
            b = i1

    print(abs(a-b))

if __name__=="__main__":
    main()
