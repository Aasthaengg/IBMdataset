import sys

def main(lines):
  N = int(lines[0])
  print(N // 2*(N - N // 2))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)