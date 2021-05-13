s = raw_input()
a,b = s.split(' ')
a,b = int(a),int(b)

def mul(a,b):
    if a <= 9 and a >=1 and (1 <= b <= 9):
        return a * b
    else:
        return -1

print mul(a,b)