n = int(input())

def isTriangular(n):
    i = 1
    while( (i*(i+1))//2 <= n) :
        if (i*(i+1))//2 == n:
            return True
        i+=1
    return False


def solve(n):
    if not isTriangular(n):
        print("No")
        return
    i = 1
    jump = 2
    ans = [[1],[1]]
    while ans[-1][-1] != n:
        next_ind = list(range(ans[-1][-1]+1, ans[-1][-1]+jump+1))
        for i in range(len(next_ind)):
            ans[i].append(next_ind[i])
        ans.append(next_ind)
        i+=jump
        jump += 1
    print("Yes")
    print(len(ans))
    for x in ans:
        p_str = ""
        p_str += str(len(x))
        for b in x:
            p_str += " " 
            p_str += str(b)
        print(p_str)
solve(n)

    
