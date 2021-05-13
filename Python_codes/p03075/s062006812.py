A = [int(input()) for _ in range(6)]

def check():
    if A[-2]-A[0]>A[-1]:
        return ':('
    return 'Yay!'
print(check())