import re

def main():
    S = input()
    print('YES' if re.match(r'^(dream|dreamer|erase|eraser)*$', S) else "NO")

main()  