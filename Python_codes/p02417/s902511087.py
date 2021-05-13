import sys
import string

def main():
    chars = {x:0 for x in string.ascii_lowercase}

    for line in sys.stdin:
        for ch in line.lower():
            if ch in chars:
                chars[ch] += 1

    for ch in string.ascii_lowercase:
        print(ch+" : "+str(chars[ch]))

if __name__ == '__main__':
    main()
