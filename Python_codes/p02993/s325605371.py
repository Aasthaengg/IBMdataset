def main():
    S = input()
    t = 'a'
    for c in S:
        if t == c:
            return False
        t = c
    return True
if main():
    print('Good')
else:
    print('Bad')
