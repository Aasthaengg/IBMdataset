n = int(input())
AL = [chr(ord('a') + i) for i in range(26)]

def number_to_alphabet(n):
    N = n-1
    a = ''
    while True:
        d = N % 26
        a = AL[d]+ a
        if N == 0: break
        N = N//26-1
        if N < 0: break
    return a

print(number_to_alphabet(n))
