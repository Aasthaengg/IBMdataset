#!/usr/bin/env python3
# -*- coding: utf-8 -*-



def main():
    T = "CODEFESTIVAL2016"

    S = input()

    ans = sum(cs != ct for cs,ct in zip(S,T))
    print(ans)

if __name__ == "__main__": main()
