def main():
    x, y, z, k = map(int, input().split())
    A = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())), reverse=True)
    C = sorted(list(map(int, input().split())), reverse=True)
    
    anslist = []
    for ai, a in enumerate(A):
        for bi, b in enumerate(B):
            for ci, c in enumerate(C):
                if (ai+1)*(bi+1)*(ci+1)<=k:
                    anslist.append(a+b+c)
                else:
                    break    
    anslist.sort(reverse=True)
    for a in anslist[:k]:
        print(a)
main()