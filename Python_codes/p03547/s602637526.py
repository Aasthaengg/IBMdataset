A,B = map(str,input().split())

def comp(A,B):
    if A > B:
        return '>'
    elif A<B:
        return '<'
    else:
        return '='

ans = comp(A,B)
print(ans)
