import sys

def solve(game: dict):
    card = game['a'].pop(0)
    while game[card]:
        card = game[card].pop(0)
    print(str.upper(card))

def main():
    game = {turn: list(sys.stdin.readline().rstrip()) for turn in 'abc'}
    solve(game)

if __name__ == '__main__':
    main()
