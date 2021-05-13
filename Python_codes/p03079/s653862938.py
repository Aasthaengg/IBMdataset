a,b,c = map(int,input().split(' '))

def judgeTriangle(a,b,c):
    if a == b == c:
        return 'Yes'
    else:
        return 'No'

print(judgeTriangle(a,b,c))