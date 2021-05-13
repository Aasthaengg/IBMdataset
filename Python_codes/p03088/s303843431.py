from functools import reduce

MOD = 1000000000 + 7
LETTERS = ["A", "C", "G", "T"]
PROHIBIT = ["AGC", "ACG", "GAC", "AGGC", "AGTC", "ATGC"]

def main():
    n = int(input().strip())

    table = {}

    for first in LETTERS:
        for second in LETTERS:
            for third in LETTERS:
                codon = first+second+third
                if not codon in PROHIBIT:
                    table[codon] = [1]

    for i in range(n-3):
        for codon in table.keys():
            table[codon].append(0)

        for codon in table.keys():
            for append in LETTERS:
                three_letters = codon[1:] + append
                four_letters = codon + append

                if (not four_letters in PROHIBIT) and (not three_letters in PROHIBIT):
                    table[three_letters][i+1] = (table[three_letters][i+1] + table[codon][i]) % MOD

    print(reduce(lambda acc, x: (acc + x[-1]) % MOD, table.values(), 0))

if __name__ == "__main__":
    main()
