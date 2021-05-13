num = int(input())
    
def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    alist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    while X_dumy>0:
        X_dumy-=1
        out = alist[(X_dumy%n)]+out
        X_dumy = int(X_dumy/n)
    return out
    
print(Base_10_to_n(num, 26))